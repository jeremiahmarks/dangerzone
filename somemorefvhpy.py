from dangerzone import fvh
from dangerzone import fvh2
from dangerzone import fvhmans

tur=fvh.MyTurtle()
tur.setup


def run1():
	tur.cleanhome()

	for x in range(1,20):
		for y in range(1,20):
			fvh.pdraw(x,y,tur)
			tur.cleanhome()
	for x in range(1,20):
		for y in range(1,20):
			fvh.pdraw(x,y,tur)
		tur.cleanhome()
	for x in range(1,20):
		for y in range(1,20):
			fvh.pdraw(x,y,tur)
	tur.cleanhome()

	for x in range(3,30,3):
		for y in range(5,75,5):
			fvh.pdraw(x,y,tur)
			tur.cleanhome()
	for x in range(3,30,3):
		for y in range(5,75,5):
			fvh.pdraw(x,y,tur)
		tur.cleanhome()
	for x in range(3,30,3):
		for y in range(5,75,5):
			fvh.pdraw(x,y,tur)
	tur.cleanhome()

	for x in range(3,30):
		fvh.coolcircles(x,tur)
		tur.cleanhome()
	for x in range(3,30):
		fvh.coolcircles(x,tur)
	tur.cleanhome()