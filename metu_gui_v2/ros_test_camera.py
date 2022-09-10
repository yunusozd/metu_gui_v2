import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray
import random

"""
Class for publishing testing camera.
"""

# https://jeffzzq.medium.com/ros2-image-pipeline-tutorial-3b18903e7329

class CameraTestPublisher(Node):

    def __init__(self):
        super().__init__('gui_camera/test_publisher')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float64MultiArray()
        msg.data = [random.random()*180 for i in range(6)]
        self.publisher_.publish(msg)
        #self.get_logger().info(f"Publishing: {msg.data}")


def main():
    rclpy.init()

    minimal_publisher = CameraTestPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()