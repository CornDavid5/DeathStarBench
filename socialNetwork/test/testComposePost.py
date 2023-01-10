import sys
sys.path.append('../gen-py')

import random
from social_network import ComposePostService
from social_network.ttypes import Media
from social_network.ttypes import PostType
from social_network.ttypes import Creator
from social_network.ttypes import Url
from social_network.ttypes import UserMention


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
  socket = TSocket.TSocket("compose-post-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = ComposePostService.Client(protocol)

  transport.open()
  req_id = random.getrandbits(63)
  client.ComposePost(req_id, "username_1", 1, "HelloWorld", [0, 1], ["png", "png"], PostType.POST, {})
  transport.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)