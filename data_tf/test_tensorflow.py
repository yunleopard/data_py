'''
Created on Nov 12, 2018

@author: yangzh
'''
# Import TensorFlow
import tensorflow as tf

# Define Constant
output = tf.constant("Hello, World")

# To print the value of constant you need to start a session.
sess = tf.Session()

# Print
print(sess.run(output))

# Close the session
sess.close()