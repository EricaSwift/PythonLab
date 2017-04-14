class A:
  def f1(self):
    print ' Class A object '
class B:
  def f1(self):
    print ' Class B object '
  def f2(self):
    print ' Class B object ' 
class C(A):
    pass    
class D(A,B):
    pass
class E(C):
    pass
class F(D):
    pass
	
a = A()
a.f1()
c = C()
c.f1()
b = B()
b.f1()
b.f2()
d = D()
d.f1()
d.f2()