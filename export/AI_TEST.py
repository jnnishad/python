import tensorflow as tf
#print ('tf.add(1,2')
##hello = tf.constant('Hello, TensorFlow!')
#print(hello.numpy())

hello = tf.constant('Hello, TensorFlow!')

sess = tf.Session()

print(sess.run(hello))
