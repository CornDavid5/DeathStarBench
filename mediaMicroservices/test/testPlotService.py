import sys
sys.path.append('../gen-py')

import random
import string
from media_service import PlotService
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def wrtie_plot():
  socket = TSocket.TSocket("plot-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = PlotService.Client(protocol)

  transport.open()
  for i in range(1, 100):
    req_id = random.getrandbits(63)
    plot_id = i
    # plot = ''.join(random.choices(string.ascii_lowercase + string.digits, k=512))
    plot = "plot: " + str(i)
    client.WritePlot(req_id, plot_id, plot, {})
  transport.close()

def read_plot():
  socket = TSocket.TSocket("plot-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = PlotService.Client(protocol)

  transport.open()
  for i in range(10):
    req_id = random.getrandbits(63)
    plot_id = random.randint(1, 99)
    client.ReadPlot(req_id, plot_id, {})
  transport.close()


if __name__ == '__main__':
  try:
    wrtie_plot()
    read_plot()
  except ServiceException as se:
    print('%s' % se.message)
  except Thrift.TException as tx:
    print('%s' % tx.message)