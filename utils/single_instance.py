import threading


# 继承元类
class SingletonMeta(type):
	"""单例模式"""
	_instances = {}
	_instance_lock = threading.Lock()

	def __call__(cls, *args, **kwargs):
		# 类调用时判断类是否在_instances中，不在_instances中时才调用
		if cls not in cls._instances:
			with SingletonMeta._instance_lock:
				if cls not in cls._instances:
					cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
		return cls._instances[cls]
