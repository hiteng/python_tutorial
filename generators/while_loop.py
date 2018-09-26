def xrange(n): #n = 5
    num = 0
    while num < n:
        yield num
        num += 1

x = xrange(5)
print x
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()

print"---------------------"


def xrange_start(st, stop):

    while st < stop:
        yield st
        st += 1

st = xrange_start(0, 5)
print st
print st.next()
print st.next()
print st.next()
print st.next()
print st.next()
print"------------------------"

def xrange_step(st, stop, step):


    while st < stop:

        yield st
        st += step


st = xrange_step(0, 20, 3)
print st
print st.next()
print st.next()
print st.next()
print st.next()
print st.next()
print st.next()
print st.next()
print"------------------------"






#Update the xrange with Start,Stop and step.

# i = 5
# for j in range(19):
#     print i
#     i = i+5