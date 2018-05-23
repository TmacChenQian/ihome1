# coding:utf-8
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """装饰器的内层函数"""
        pass
    return wrapper

class tt(object):

    @login_required
    def logout(self):
        """登出"""
        pass









# @login_required
# def logout():
#     """登出"""
#     pass


if __name__ == '__main__':
    print(logout.__name__)  # -> wrapper
    print(logout.__doc__)