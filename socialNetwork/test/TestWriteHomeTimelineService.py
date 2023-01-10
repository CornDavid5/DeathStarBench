import sys
sys.path.append('../gen-py')

import uuid
from social_network import HomeTimelineService
from social_network.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
  socket = TSocket.TSocket("home-timeline-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = HomeTimelineService.Client(protocol)

  transport.open()
  req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
  user_id = 1
  client.WriteHomeTimeline(req_id, 0, user_id, 23423423444, [0, 1], {})
  transport.close()

if __name__ == '__main__':
  try:
    main()
  except ServiceException as se:
    print('%s' % se.message)
  except Thrift.TException as tx:
    print('%s' % tx.message)