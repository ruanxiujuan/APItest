import logging

#log_level= logging.WARNING #默认warning一下级别不会输出
#Logger 日志记录器
#Handler 日志处理器
# Formatter 日志格式
#Filter 日志过滤器

cmd_handler = logging.StreamHandler()
file_handler= logging.FileHandler("4.log",encoding="utf-8")

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s %(lineno)d %(funcName)s %(levelname)s %(message)s",
                    handlers=[cmd_handler,file_handler])
# 一次运行，全局生效



logging.info("信息级别日志")
logging.warning("警告级别日志")
logging.error("错误级别日志")
logging.critical("严重错误级别日志")
