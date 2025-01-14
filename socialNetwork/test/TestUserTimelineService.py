import sys
sys.path.append('../gen-py')

import uuid
from social_network import UserTimelineService
from social_network.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
  socket = TSocket.TSocket("user-timeline-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = UserTimelineService.Client(protocol)

  transport.open()

  user_id = 1
  req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
  client.WriteUserTimeline(req_id, 1, user_id, 324324234, {})

  req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
  start = 0
  stop = 5
  client.ReadUserTimeline(req_id, user_id, start, stop, {})
  transport.close()

if __name__ == '__main__':
  try:
    main()
  except ServiceException as se:
    print('%s' % se.message)
  except Thrift.TException as tx:
    print('%s' % tx.message)