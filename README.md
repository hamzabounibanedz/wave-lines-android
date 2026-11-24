<!-- independent-distribution -->
# WaveLinesWallpaper for Android

Customizable animated wave wallpapers. This independently signed edition builds the [original 1.13.7 release](https://github.com/markusfisch/WaveLinesWallpaper/tree/b65e2cdef3884aece57c5cb84963d38663693415) from source. The upstream name, license and application features are preserved.

[Download APK and AAB](https://github.com/hamzabounibanedz/wave-lines-android/releases/latest) · [Cloud build and emulator results](https://github.com/hamzabounibanedz/wave-lines-android/actions/workflows/distribution.yml)

![Scan for the Android installation page](distribution/install-qr.png)

Download the APK on your phone and open it. Android may ask you to allow the download source to install apps. This edition uses its own Android package ID, `io.github.hamzabounibanedz.wavelines`, and signing certificate. It can be installed alongside the original app. GitHub Actions assigns an increasing Android version code to each new build.

Run **Actions → Build, test and release Android → Run workflow** to compile, sign, install and test on a hosted Android emulator, and publish a new release. The release includes the APK, AAB, SHA-256 checksums, installation QR and device evidence. Repository signing secrets are ANDROID_KEYSTORE and ANDROID_KEYPASS. No backend or login is required.

## Upstream documentation

# Wave Lines Live Wallpaper

An Android live wallpaper showing slowly moving wave lines.

Either choose a predefined theme, edit a theme to your liking, or simply
create your own.

If you find this app useful and wish to support its continued development,
you can [buy me a coffee](https://www.buymeacoffee.com/markusfisch) or
send some Bitcoin decimals to `bc1q2guk2rpll587aymrfadkdtpq32448x5khk5j8z`.

<a href="https://www.buymeacoffee.com/markusfisch" target="_blank"><img
	src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
	alt="Buy Me A Coffee"
	style="height: 60px !important;width: 217px !important;"/></a>&nbsp;<a
	href="https://liberapay.com/markusfisch/" target="_blank"><img
	src="https://liberapay.com/assets/widgets/donate.svg"
	alt="Liberapay"
	style="height: 60px !important"/></a>&nbsp;<a
	href="https://ko-fi.com/markusfisch" target="_blank"><img
	src="https://storage.ko-fi.com/cdn/brandasset/kofi_s_tag_dark.png"
	alt="Ko-fi"
	style="height: 60px !important"/></a>

## Screenshots

<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/screencap-gallery.png"
	alt="Screenshot Gallery" width="160"/>
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/screencap-theme.png"
	alt="Screenshot Theme" width="160"/>
<img src="fastlane/metadata/android/en-US/images/phoneScreenshots/screencap-editor.png"
	alt="Screenshot Editor" width="160"/>

## Download

<a href="https://f-droid.org/packages/de.markusfisch.android.wavelines/"><img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png"
	alt="Get it on F-Droid" height="80"></a>
<a href="https://play.google.com/store/apps/details?id=de.markusfisch.android.wavelines"><img
	src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png"
	alt="Get it on Google Play" height="80"></a>
