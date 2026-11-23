import json, math, os, sys
# Colours from brand/tokens.json: gold is Physics primaryDeep; the second arrow colour is
# Physics secondary (violet), replacing an off-palette blue (2026-11-23, Matt's choice).
_T = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "brand", "tokens.json"), encoding="utf-8"))
_P = _T["courses"]["physics"]
th=math.radians(30); INK="#222"; GOLD=_P["primaryDeep"]["hex"]; BLUE=_P["secondary"]["hex"]; GREY="#999"
out=[]
def A(s): out.append(s)
def line(p,q,c=INK,w=3,dash=None): A(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{c}" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def arrow(p,q,c=INK,w=4):
    line(p,q,c,w); ang=math.atan2(q[1]-p[1],q[0]-p[0]); L=18; s=0.42
    a=(q[0]-L*math.cos(ang-s),q[1]-L*math.sin(ang-s)); b=(q[0]-L*math.cos(ang+s),q[1]-L*math.sin(ang+s))
    A(f'<polygon points="{q[0]:.1f},{q[1]:.1f} {a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f}" fill="{c}"/>')
def text(p,t,size=22,c=INK,w="normal",anchor="start"): A(f'<text x="{p[0]:.1f}" y="{p[1]:.1f}" font-size="{size}" fill="{c}" font-weight="{w}" text-anchor="{anchor}">{t}</text>')
def arc(c,r,a0,a1,col=GOLD,w=3):
    # angles in math degrees (y up); svg y down
    p0=(c[0]+r*math.cos(math.radians(a0)),c[1]-r*math.sin(math.radians(a0)))
    p1=(c[0]+r*math.cos(math.radians(a1)),c[1]-r*math.sin(math.radians(a1)))
    large=1 if abs(a1-a0)>180 else 0; sweep=0 if a1>a0 else 1
    A(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 {large} {sweep} {p1[0]:.1f},{p1[1]:.1f}" fill="none" stroke="{col}" stroke-width="{w}"/>')
def P(x,y,ox,oy,s): return (ox+x*s, oy-y*s)   # math coords -> svg
W_,H_=1100,850
A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W_}" height="{H_}" viewBox="0 0 {W_} {H_}" font-family="Archivo"><rect width="100%" height="100%" fill="white"/>')
text((W_/2,50),"Why sin goes DOWN the ramp and cos goes INTO the ramp",30,INK,"bold","middle")
# Panel 1
ox,oy,s=40,590,60
u=(math.cos(th),math.sin(th)); n=(-math.sin(th),math.cos(th))
base=(0,0); top=(9,0); peak=(9,9*math.tan(th))
A('<polygon points="'+" ".join(f"{P(*q,ox,oy,s)[0]:.1f},{P(*q,ox,oy,s)[1]:.1f}" for q in (base,top,peak))+f'" fill="none" stroke="{INK}" stroke-width="4"/>')
arc(P(0,0,ox,oy,s),75,0,30); text(P(1.35,0.22,ox,oy,s),"θ",30,GOLD,"bold")
c=(u[0]*6.6+n[0]*0.6, u[1]*6.6+n[1]*0.6)
def r(v): return (math.cos(th)*v[0]-math.sin(th)*v[1], math.sin(th)*v[0]+math.cos(th)*v[1])
box=[(c[0]+r(v)[0],c[1]+r(v)[1]) for v in ((-.6,-.6),(.6,-.6),(.6,.6),(-.6,.6))]
A('<polygon points="'+" ".join(f"{P(*q,ox,oy,s)[0]:.1f},{P(*q,ox,oy,s)[1]:.1f}" for q in box)+f'" fill="none" stroke="{INK}" stroke-width="4"/>')
W=2.9; fg=(c[0],c[1]-W)
par=(c[0]-u[0]*W*math.sin(th), c[1]-u[1]*W*math.sin(th)); perp=(c[0]-n[0]*W*math.cos(th), c[1]-n[1]*W*math.cos(th))
line(P(*par,ox,oy,s),P(*fg,ox,oy,s),GREY,2,"8,6"); line(P(*perp,ox,oy,s),P(*fg,ox,oy,s),GREY,2,"8,6")
arrow(P(*c,ox,oy,s),P(*fg,ox,oy,s),INK,5); text(P(fg[0]+0.15,fg[1]-0.35,ox,oy,s),"Fg = mg",26,INK,"bold")
arrow(P(*c,ox,oy,s),P(*par,ox,oy,s),BLUE,4); text(P(par[0]-2.55,par[1]+0.55,ox,oy,s),"mg sin θ",24,BLUE,"bold"); text(P(par[0]-2.55,par[1]+0.12,ox,oy,s),"down the ramp",19,BLUE)
arrow(P(*c,ox,oy,s),P(*perp,ox,oy,s),BLUE,4); text(P(perp[0]+0.3,perp[1]+0.1,ox,oy,s),"mg cos θ",24,BLUE,"bold"); text(P(perp[0]+0.3,perp[1]-0.32,ox,oy,s),"into the ramp",19,BLUE)
a0=-90; a1=math.degrees(math.atan2(-n[1],-n[0])); arc(P(*c,ox,oy,s),62,a0,a1)
m=math.radians((a0+a1)/2); text(P(c[0]+1.35*math.cos(m)-0.15,c[1]+1.35*math.sin(m)-0.25,ox,oy,s),"θ",28,GOLD,"bold")
text((40,110),"1  Draw Fg straight down. Split it along and into the ramp.",21,INK,"bold")
text((40,138),"The SAME angle θ shows up between Fg and the “into the ramp” line.",19,INK)
# Panel 2: level the ramp
ox2,oy2,s2=890,250,62
text((690,110),"2  Turn the page so the ramp is level.",21,INK,"bold")
text((690,138),"Now it's a normal triangle.",19,INK)
text((690,162),"cos stays CLOSE to θ.",19,GOLD,"bold")
o=(0,0); W2=4.2
fgv=(math.sin(th)*W2*-1, -math.cos(th)*W2)   # tilted Fg, down-left
pp=(0,-W2*math.cos(th)); pl=(fgv[0],0)
line(P(*pl,ox2,oy2,s2),P(*fgv,ox2,oy2,s2),GREY,2,"8,6"); line(P(*pp,ox2,oy2,s2),P(*fgv,ox2,oy2,s2),GREY,2,"8,6")
arrow(P(*o,ox2,oy2,s2),P(*fgv,ox2,oy2,s2),INK,5); text(P(fgv[0]-0.2,fgv[1]-0.45,ox2,oy2,s2),"Fg",26,INK,"bold","middle")
arrow(P(*o,ox2,oy2,s2),P(*pp,ox2,oy2,s2),BLUE,4); text(P(0.2,pp[1]*0.55,ox2,oy2,s2),"cos θ",24,BLUE,"bold"); text(P(0.2,pp[1]*0.55-0.42,ox2,oy2,s2),"(next to θ)",18,BLUE)
arrow(P(*o,ox2,oy2,s2),P(*pl,ox2,oy2,s2),BLUE,4); text(P(pl[0]*0.5,0.35,ox2,oy2,s2),"sin θ  (across from θ)",20,BLUE,"bold","middle")
arc(P(*o,ox2,oy2,s2),70,-90,math.degrees(math.atan2(fgv[1],fgv[0]))); text(P(-0.62,-1.55,ox2,oy2,s2),"θ",28,GOLD,"bold")
text(P(pl[0]*0.5,0.85,ox2,oy2,s2),"(down the ramp)",16,GREY,"normal","middle")
# Panel 3: table
y0=640; text((40,y0),"3  Check the extremes. Don't memorize it — check it.",21,INK,"bold")
cols=[40,250,520,690,960]
rows=[["Ramp angle","Down the ramp should be…","sin θ","Into the ramp should be…","cos θ"],
["0°  flat floor","nothing (it doesn't slide)","sin 0° = 0 ✓","the whole weight","cos 0° = 1 ✓"],
["90°  vertical wall","the whole weight (it falls)","sin 90° = 1 ✓","nothing (no pressing)","cos 90° = 0 ✓"]]
for i,rw in enumerate(rows):
    y=y0+42+i*44
    for x,t in zip(cols,rw): text((x,y),t,19 if i else 18,INK,"bold" if i==0 else "normal")
    if i==0: line((40,y+12),(1060,y+12),GREY,1.5)
A('</svg>'); open(sys.argv[1],"w").write("\n".join(out))
