import tensorflow as tf

a = tf.constant(5);
b = tf.constant(2)
c = tf.constant(3);

d = tf.multiply(a,b)
e = tf.add(c,b)
f = tf.subtract(d,e)


sess= tf.Session()
outs = sess.run(f)
sess.close()

print outs


a = tf.constant(10)
b = tf.constant(20)
d = tf.add(a,b)
c = tf.multiply(a,b)
f = tf.add(d,c)
e= tf.subtract(d,c)


print(tf.get_default_graph())
g	=	tf.Graph()
print(g)

ae	=	tf.constant(5)
print(ae.graph	is	g)
print(ae.graph	is	tf.get_default_graph())





