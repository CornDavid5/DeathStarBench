import sys
sys.path.append('../gen-py')

import uuid
from social_network import UrlShortenService
from social_network.ttypes import Url

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
  socket = TSocket.TSocket("url-shorten-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = UrlShortenService.Client(protocol)

  transport.open()
  req_id = uuid.uuid4().int & ( 1 << 32 )
  urls = ["https://url_0.com", "https://url_1.com", "https://url_2.com"]
  urls = client.ComposeUrls(req_id, urls, {})

  urls = [url.shortened_url for url in urls]
  req_id = uuid.uuid4().int & ( 1 << 32 )
  client.GetExtendedUrls(req_id, urls, {})
  transport.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)