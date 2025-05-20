from std_srvs.srv import SetBool
from mavros_msgs.msg import OverrideRCIn
import rclpy
from rclpy.node import Node

class GarraService(Node):
    def __init__(self):
        super().__init__('garra_service')
        self.srv = self.create_service(SetBool, 'garra_control', self.garra_callback)
        self.pub = self.create_publisher(OverrideRCIn, '/mavros/rc/override', 10)

        # PWM para abrir y cerrar la garra (ajústalos según tu configuración)
        self.garra_abierta_pwm = 1900
        self.garra_cerrada_pwm = 1100
        self.canal_garra = 9  # Canal en el PX4 al que está conectada la garra

        self.get_logger().info('Servicio de la garra listo')

    def garra_callback(self, request, response):
        pwm = self.garra_abierta_pwm if request.data else self.garra_cerrada_pwm
        msg = OverrideRCIn()
        msg.channels = [0] * 18 #poner 18 canales control en estado 0 (sin overide segun mavros)
        
        msg.channels[self.canal_garra] = pwm

        self.pub.publish(msg)

        estado = 'abierta 👋' if request.data else 'cerrada ✊'
        self.get_logger().info(f'Garra {estado}')

        response.success = True
        response.message = f'Garra {estado}'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = GarraService()
    rclpy.spin(node)
    rclpy.shutdown()
