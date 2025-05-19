import rclpy
from rclpy.node import Node
import cv2
from std_msgs.msg import String
from football_tracker.color_utils import get_color_ranges

class TrackerNode(Node):
    def __init__(self):
        super().__init__('tracker_node')
        self.publisher_ = self.create_publisher(String, 'ball_color', 10)
        self.cap = cv2.VideoCapture(0)  # Usa la cámara por defecto
        self.color_ranges = get_color_ranges()
        self.timer = self.create_timer(0.1, self.detect_ball)

    def detect_ball(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn('No se pudo leer la cámara.')
            return

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        found_color = 'desconocido'

        for color, ranges in self.color_ranges.items():
            for lower, upper in ranges:
                mask = cv2.inRange(hsv, lower, upper)
                contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                if contours and cv2.contourArea(max(contours, key=cv2.contourArea)) > 500:
                    found_color = color
                    break

        self.publisher_.publish(String(data=found_color))
        cv2.imshow("Ball Tracker", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = TrackerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
