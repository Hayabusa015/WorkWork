"""Draw VSEPR shapes from real 3D geometry (true bond angles), projected to SVG."""
import math, sys
s3=math.sqrt(3)
def ry(v,a):
    a=math.radians(a);x,y,z=v;return (x*math.cos(a)+z*math.sin(a),y,-x*math.sin(a)+z*math.cos(a))
def rx(v,a):
    a=math.radians(a);x,y,z=v;return (x,y*math.cos(a)-z*math.sin(a),y*math.sin(a)+z*math.cos(a))
def norm(v):
    m=math.sqrt(sum(c*c for c in v));return tuple(c/m for c in v)
# base electron geometries (unit vectors)
r=math.sqrt(8)/3
TET=[(0,1,0)]+[(r*math.sin(math.radians(p)),-1/3,r*math.cos(math.radians(p))) for p in (0,120,240)]
c,s=math.cos(math.radians(54.7356)),math.sin(math.radians(54.7356))
TET_B=[(s,-c,0),(-s,-c,0),(0,c,s),(0,c,-s)]          # edge-on view for bent
TRI=[(0,1,0),(-s3/2,-.5,0),(s3/2,-.5,0)]
TBP=[(0,1,0),(0,-1,0)]+[(math.sin(math.radians(p)),0,math.cos(math.radians(p))) for p in (90,210,330)]
OCT=[(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
LIN=[(1,0,0),(-1,0,0)]
# key: (domains, lone pairs) -> (vectors, lone-pair indices, yaw, tilt)
SHAPES={
 (2,0):(LIN,[],0,0),
 (3,0):(TRI,[],0,0),(3,1):(TRI,[0],0,0),
 (4,0):(TET,[],270,14),(4,1):(TET,[0],270,14),(4,2):(TET_B,[2,3],38,0),
 (5,0):(TBP,[],-8,24),(5,1):(TBP,[2],-8,24),(5,2):(TBP,[3,4],-8,24),(5,3):(TBP,[2,3,4],-8,24),
 (6,0):(OCT,[],32,22),(6,1):(OCT,[1],32,22),(6,2):(OCT,[0,1],32,22),
}
ORANGE="#FF6B1A";INK="#2E3338";LOBE="#E9F8FC"
def svg(key,W=170,H=128,L=47):
    vecs,lps,yaw,tilt=SHAPES[key]
    cx,cy=W/2,H/2+2
    P=lambda v:(cx+v[0]*L*(1+.06*v[2]),cy-v[1]*L*(1+.06*v[2]))
    items=[]
    for i,v in enumerate(vecs):
        w=rx(ry(norm(v),yaw),tilt)
        if i in lps:
            ctr=tuple(.80*k for k in w); px,py=P(ctr)
            dx,dy=w[0],-w[1]; pl=math.hypot(dx,dy)
            ang=math.degrees(math.atan2(dy,dx)) if pl>1e-6 else 0
            rmaj=max(.42*L*pl,.27*L); rmin=.2*L
            g=(f'<g transform="translate({px:.1f},{py:.1f}) rotate({ang:.1f})">'
               f'<ellipse rx="{rmaj:.1f}" ry="{rmin:.1f}" fill="{LOBE}" stroke="{INK}" stroke-width="1.1" stroke-dasharray="3 2.2"/>'
               f'<circle cx="0" cy="-4" r="2.1" fill="{INK}"/><circle cx="0" cy="4" r="2.1" fill="{INK}"/></g>')
            items.append((w[2]*.8,g))
        else:
            ex,ey=P(w); sw=4.2+1.2*w[2]
            items.append((w[2]*.5,f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{INK if w[2]>-.3 else '#7A8086'}" stroke-width="{sw:.1f}" stroke-linecap="round"/>'))
            rad=9*(1+.12*w[2])
            items.append((w[2],f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="{rad:.1f}" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'))
    items.append((0.001,f'<circle cx="{cx}" cy="{cy}" r="12" fill="{ORANGE}" stroke="{INK}" stroke-width="1.6"/>'))
    items.sort(key=lambda t:t[0])
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'+''.join(g for _,g in items)+'</svg>'
