# -*- coding: utf-8 -*-
# time: 2019/4/17 下午1:51
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

StatusCode = int

status_codes = {
    0: ("SUCC", dict(zh="成功",
                     en='Success')),
    1: ("E_PARAM", dict(zh="参数错误",
                        en="Parameter error")),
    1001: ("E_USER_NOT_LOGIN", dict(zh='请先登录',
                                    en='Please sign in first')),
    1002: ("E_PERMISSION_DENIED", dict(zh='无操作权限',
                                       en='No operation permission')),
    1003: ("E_SOURCE_NOT_FOUND", dict(zh='资源不存在',
                                      en='Source not found')),
    1004: ("E_INVALID_PASSWORD", dict(zh='密码错误',
                                      en='Password is wrong')),
    1005: ("E_USER_NOT_EXISTS", dict(zh='用户不存在',
                                     en='Account not found'))
}


def set_values_into_global(dest: dict):
    for k, v in status_codes.items():
        dest.update({v[0]: k})


def aggregate_status_code():
    path = Path(__file__).parent.parent.joinpath("app/config/status_code").resolve()
    specs = map(lambda i: spec_from_file_location(i.name, i.as_posix()),
                filter(lambda i: not i.name.startswith("__"), path.iterdir()))
    specs = list(specs)
    modules = map(lambda i: module_from_spec(i), specs)
    modules = list(modules)

    list(map(lambda s, m: s.loader.exec_module(m), specs, modules))
    for m in modules:
        status_code = m.status_code
        status_codes.update(status_code)


# aggregate_status_code()
set_values_into_global(globals())

if __name__ == "__main__":
    import_module = __import__(__name__)
    print(import_module.E_STYLE_EXISTS)
