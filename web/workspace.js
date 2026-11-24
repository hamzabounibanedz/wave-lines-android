import {$,read,save,download} from './ui.js';
const palettes={'Sea glass':['#093b4d','#126176','#329497','#7ecebb','#e0e9bf'],'Dusk coral':['#49283f','#864257','#c46969','#f5b082','#f9d5ad'],'Deep indigo':['#191834','#2f355f','#506391','#8fa3c6','#d9d9e8']};
const state=read('tideglass-settings',{palette:'Sea glass',height:23,layers:12,seed:17});
const canvas=$('#waves'),ctx=canvas.getContext('2d');
function draw(){
 const colors=palettes[state.palette],w=canvas.width,h=canvas.height,n=state.layers,phase=state.seed*.19;
 const sky=ctx.createLinearGradient(0,0,w,h);sky.addColorStop(0,colors[0]);sky.addColorStop(1,colors[2]);ctx.fillStyle=sky;ctx.fillRect(0,0,w,h);
 for(let k=0;k<n;k++){const y=h*(.1+.88*k/n);
  const grad=ctx.createLinearGradient(0,y,w,y+h/n);grad.addColorStop(0,colors[1+k%4]);grad.addColorStop(1,colors[k%4]);ctx.fillStyle=grad;ctx.beginPath();
  for(let x=0;x<=w;x+=6){const t=x/w,dy=state.height*4*(Math.sin(t*5.3+phase+k*.29)+.32*Math.sin(t*10-k*.37+phase));if(x===0)ctx.moveTo(x,y+dy);else ctx.lineTo(x,y+dy)}
  ctx.lineTo(w,h);ctx.lineTo(0,h);ctx.closePath();ctx.fill();
 }
 $('#heightValue').textContent=state.height;$('#layerValue').textContent=n;$('#caption').textContent=state.palette+' / '+String(state.seed).padStart(3,'0');
 const chips=$('#swatches');chips.replaceChildren();for(const c of colors){const i=document.createElement('i');i.style.background=c;chips.append(i)}
}
for(const field of ['palette','height','layers']){const control=$('#'+field);control.value=state[field];control.oninput=()=>{state[field]=field==='palette'?control.value:Number(control.value);save('tideglass-settings',state);draw()}}
$('#shift').onclick=()=>{state.seed=state.seed%999+1;save('tideglass-settings',state);draw()};$('#export').onclick=()=>download(canvas,'tideglass-'+state.seed+'.png');draw();
