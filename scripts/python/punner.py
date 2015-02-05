from funpun import point
import funpun
point1=point()
point2=point()
point1.x,point1.y,point2.x,point2.y=funpun.getpoints()
distance=funpun.distance(point1,point2)
input(distance)

