"""Run against the installed release APK on a disposable hosted Android emulator."""
import json
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path

PACKAGE = 'de.markusfisch.android.wavelines'
EVIDENCE = Path('delivery/evidence')
EVIDENCE.mkdir(parents=True, exist_ok=True)
checks = []

def adb(*args):
    return subprocess.check_output(['adb', *args], text=True, timeout=60).strip()

def shell(*args):
    return adb('shell', *args)

def record(description):
    checks.append(description)
    print('PASS', description, flush=True)

def capture(name):
    (EVIDENCE / (name + '.png')).write_bytes(subprocess.check_output(['adb','exec-out','screencap','-p']))

def screen():
    shell('uiautomator','dump','/sdcard/distribution-window.xml')
    xml = adb('exec-out','cat','/sdcard/distribution-window.xml')
    (EVIDENCE/'last-screen.xml').write_text(xml)
    return list(ET.fromstring(xml).iter('node'))

def find(value, timeout=25):
    deadline=time.monotonic()+timeout
    while time.monotonic()<deadline:
        try:
            for node in screen():
                a=node.attrib
                if value in (a.get('text'),a.get('content-desc'),a.get('resource-id'),a.get('resource-id','').split('/')[-1]):
                    return a
        except (ET.ParseError, subprocess.SubprocessError): pass
        time.sleep(.4)
    raise AssertionError('Missing screen element '+value)

def tap(value):
    x1,y1,x2,y2=map(int,re.findall(r'\d+',find(value)['bounds']))
    shell('input','tap',str((x1+x2)//2),str((y1+y2)//2))
    time.sleep(.45)

def launch():
    shell('monkey','-p',PACKAGE,'-c','android.intent.category.LAUNCHER','1')
    time.sleep(2)
    assert shell('pidof',PACKAGE), 'No application process'
    
def activity(name):
    deadline=time.monotonic()+25
    while time.monotonic()<deadline:
        focus=shell('dumpsys','activity','activities')
        if any(name in line and ('mResumed' in line or 'topResumed' in line) for line in focus.splitlines()): return
        time.sleep(.5)
    raise AssertionError('Expected foreground activity '+name)

def exercise():
    tap('add_theme')
    bounds=find('themes')['bounds']
    x1,y1,x2,y2=map(int,re.findall(r'\d+',bounds))
    shell('input','tap',str(x1+(x2-x1)//4),str(y1+100))
    activity('ThemeActivity')
    find('set_theme')
    record('Added a wallpaper theme and opened its preview and apply controls')

try:
    apk=next(Path('delivery').glob('*.apk'))
    assert 'Success' in adb('install','-g',str(apk))
    assert 'package:' in shell('pm','path',PACKAGE)
    record('Signed release APK installed on Android '+shell('getprop','ro.build.version.release'))
    shell('wm','size','720x1440')
    shell('wm','density','300')
    shell('input','keyevent','KEYCODE_WAKEUP')
    shell('wm','dismiss-keyguard')
    adb('logcat','-c')
    launch()
    capture('01-launch')
    exercise()
    capture('02-workflow')
    crashes=adb('logcat','-d','-b','crash')
    assert 'Process: '+PACKAGE+',' not in crashes, crashes
    record('No application crash in the device crash buffer during the test')
finally:
    capture('last-frame')
    (EVIDENCE/'checks.json').write_text(json.dumps(checks,indent=2))
    (EVIDENCE/'crash-log.txt').write_text(adb('logcat','-d','-b','crash'))

