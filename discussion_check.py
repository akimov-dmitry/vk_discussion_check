import vk
import time
import sys
import urllib
import threading
import socket
import requests
session = vk.Session(access_token='')
api = vk.API(session)

gr_id = input("Enter group id: ") # gr_id = group_id in api.board.GetComments method
top_id = input("Enter discussion id: ") # top_id = topic_id in api.board.getComments method
#pr_id = input("Enter user id for messaging: ") # pr_id = peer_id in api.messages.send method
com_id = input("Enter start comment id: ") # Declare comment id to start from

i=1

while True:
    try:
    
        old_state = api.board.getComments(group_id=gr_id, topic_id=top_id, start_comment_id=com_id, count=100, v=5.33)
        time.sleep(1)
        new_state = api.board.getComments(group_id=gr_id, topic_id=top_id, start_comment_id=com_id, count=100, v=5.33)
        if old_state!=new_state:
            #api.messages.send(user_id = pr_id, message= 'New comment:', v=5.38)
            print("New comment:")
            #print(type(new_state))
            #print(new_state.keys())
            comment_info = new_state.get('items')
            #print(type(comment_info))

            #-*-comment_text_dict = comment_info[i]
            if i==100:
                com_id=com_id+100
                i=1
            else:
                i=i+1

            comment_text_dict=comment_info.pop()
            #print(comment_text_dict)
            #print(type(comment_text_dict))
            comment_text=comment_text_dict.get('text')
            print(comment_text)
            continue
    
    except requests.packages.urllib3.exceptions.ReadTimeoutError:
        print("ReadTimeoutError")
        continue
    except requests.exceptions.ReadTimeout:
        print("ReadTimeout")
        continue
    except:
        print("SocketTimeout")
        continue

