import logging

# log_level 默认为 logging.WARNING

cmd_handler = logging.StreamHandler()
file_handler = logging.FileHandler("2.log", encoding="utf-8")


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s %(lineno)d %(funcName)s %(levelname)s %(message)s",
                    handlers=[cmd_handler, file_handler])

# Logger 日志记录器 root
# Handler 日志处理器
# Formatter 日志格式
# Filter 日志过滤器


logging.debug("调试级别的日志")
logging.info("信息级别的日志")
logging.warning("警告级别的日志")
logging.error("错误级别的日志")
logging.critical("严重错误级别的日志")