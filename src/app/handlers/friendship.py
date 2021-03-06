# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
from ..net.msg_handler import msg_handler
from ..dao.message import MessageDao


@msg_handler.on("friends_add")
def friends_add(conn, manager, data):
    print "friends add", data
    try:
        if not data:
            raise Exception("data not found")
        send_to = data.get("username")
        content = data.get("content")
        send_from = conn.get_user().username
        print send_from
        send_to_conn = manager.getConnectionByUsername(send_to)
        if send_to_conn:
            send_to_conn.send({
                "cmd": "new_message",
                "data": {
                    "retcode": 0,
                    "result": [{
                        "type": "friends_add",
                        "send_from": send_from,
                        "send_to": send_to,
                        "content": content
                    }]}})
        else:
            ret = MessageDao.message_add(type="friends_add", send_from=send_from, send_to=send_to, content=content)
            print ret
        conn.send({"cmd": "friends_add", "data": {"retcode": 0, "result": "success"}})
    except Exception, e:
        print e
        conn.send({"cmd": "friends_add", "data": {"retcode": -1, "errmsg": e.message}})


@msg_handler.on("friends_list")
def friends_list(conn, manager, data):
    print data
    pass


@msg_handler.on("friends_remove")
def friends_remove(conn, manager, data):
    print data
    pass
