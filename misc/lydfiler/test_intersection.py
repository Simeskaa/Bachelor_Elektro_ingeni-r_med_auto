from PySide6.QtCore import QLineF, QPointF

p1 = QPointF(0,0)
p2 = QPointF(1000000,1000000)
p3 = QPointF(0,1000)
p4 = QPointF(1000,0)

L1 = QLineF(p1,p2)
L2 = QLineF(p4,p3)

#print(L1.intersects(L2))

print(f'm2 avr: {(77.31975447973662 + 77.42558963291344 + 77.152177800181) / 3}'
      f'\nm1 avr: {(77.90911880138916 + 77.42558963291344)/2}'
      f'\nm4 avr: {77.15217780018097}'
      f'\nU: {77.34744349944202}')

