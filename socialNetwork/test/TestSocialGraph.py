import sys
sys.path.append('../gen-py')

import uuid
from social_network import SocialGraphService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
  socket = TSocket.TSocket("social-graph-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = SocialGraphService.Client(protocol)

  transport.open()
  req_id = uuid.uuid4().int & (1<<32)
  client.InsertUser(req_id, 999, {})
  client.Follow(req_id, 0, 1, {})
  client.Follow(req_id, 0, 2, {})
  client.Follow(req_id, 1, 2, {})
  client.Follow(req_id, 1, 0, {})
  client.Follow(req_id, 2, 1, {})
  client.Follow(req_id, 2, 0, {})
  client.Unfollow(req_id, 1, 0, {})
  client.FollowWithUsername(req_id, "username_1", "username_0", {})
  client.Unfollow(req_id, 1, 2, {})
  client.UnfollowWithUsername(req_id, "username_1", "username_0", {})
  client.Follow(req_id, 1, 0, {})
  client.Follow(req_id, 1, 2, {})

  client.GetFollowers(req_id, 0, {})
  client.GetFollowers(req_id, 1, {})
  client.GetFollowers(req_id, 2, {})
  client.GetFollowees(req_id, 0, {})
  client.GetFollowees(req_id, 1, {})
  client.GetFollowees(req_id, 2, {})

  transport.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)