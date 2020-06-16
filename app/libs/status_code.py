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
                                     en='Account not found')),
    1006: ("E_FILE_NOT_EXISTS", dict(zh='文件不存在',
                                     en='File not found')),
    1007: ("E_TASK_NOT_EXISTS", dict(zh='任务不存在',
                                     en='Task not found')),
    1008: ("E_ILLEGAL_FILE_FORMAT", dict(zh="非法的文件格式",
                                         en="illegal file format")),
    1009: ("E_PATH_NOT_FILE", dict(zh="路径非文件",
                                   en="path is not a file")),
    1010: ("E_PATH_NOT_DIR", dict(zh="路径非文件夹",
                                  en="path is not a directory")),
    1011: ("E_NO_VALID_CONFIG_FILE", dict(zh="无有效配置文件",
                                          en="no valid config file")),
    1012: ("E_ILLEGAL_DIR_FORMAT", dict(zh="文件夹格式错误",
                                        en="illegal dir format")),
    2002: ("E_INSUFFICIENT_PARAM", dict(zh='请求参数不完整',
                                        en='Request parameters are incomplete')),
    2003: ("E_REQUEST_ERROR", dict(zh='请求出错，请稍后再试',
                                   en='Request error, please try again later')),
    2004: ("E_PARAM_ILLEGAL", dict(zh='请求参数不合法',
                                   en='Request parameter is invalid')),
    2005: ("E_REPEAT_CALL", dict(zh='请勿重复调用',
                                 en='please don not re-use')),
    2006: ("E_IMAGE_SERVER_ERROR", dict(zh="图片服务不可用",
                                        en='Image Server Stopped!')),
    2007: ("E_NO_CONTENT", dict(zh="无内容",
                                en="No content")),
    3000: ("E_PROJECT_EXISTS", dict(zh="工程已存在",
                                    en="Project exists")),
    3001: ("E_PROJECT_NOT_EXISTS", dict(zh='工程不存在',
                                        en='Project not exists')),
    3002: ("E_DELETE_PROJECT_FAILED", dict(zh="删除工程失败",
                                           en="delete project failed")),
    4000: ("E_CATEGORY_NOT_EXISTS", dict(zh='类别不存在',
                                         en='Category not exists')),
    4001: ("E_CATEGORY_EXISTS", dict(zh='类别已存在',
                                     en='Category exists')),
    4002: ("E_BUILTIN_TYPE_DELETE_DENIED", dict(zh="内置类别不支持删除",
                                                en="Builtin categories couldn't delete")),
    5000: ("E_SUPERVISOR_STATUS_ERROR", dict(zh="supervisor状态异常",
                                             en="supervisor status error")),
    6000: ("E_PLUGIN_EXISTS", dict(zh="插件已存在",
                                   en="plugin exists")),
    6001: ("E_PLUGIN_NOT_EXISTS", dict(zh="插件不存在",
                                       en="plugin Not exists")),
    9999: ("E_UNKNOWN_ERROR", dict(zh='未知的错误',
                                   en='Unknown error')),
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
