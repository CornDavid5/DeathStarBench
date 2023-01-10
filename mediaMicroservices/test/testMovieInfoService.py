import sys
sys.path.append('../gen-py')

import random
import string
from media_service import MovieInfoService
from media_service.ttypes import Cast
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def wrtie_movie_info():
  socket = TSocket.TSocket("movie-info-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = MovieInfoService.Client(protocol)

  transport.open()
  for i in range(100000, 100005):
    req_id = random.getrandbits(63)
    movie_id = "movie_id_" + str(i)
    title = "movie_" + str(i)
    cast_id = random.randint(0, 96)
    casts = []
    for j in range(3):
      cast = Cast(cast_id=j, character="character_"+str(j), cast_info_id=cast_id+j)
      casts.append(cast)
    plot_id = i
    thumbnail_ids = []
    photo_ids = []
    video_ids = []
    # for j in range(1):
      # thumbnail_ids.append(u'25.0')
      # photo_ids.append(u'25.0')
      # video_ids.append(u'25.0')
    avg_rating = random.randint(0, 10)
    num_rating = random.randint(1, 100)
    client.WriteMovieInfo(req_id, movie_id, title, casts, plot_id, thumbnail_ids, photo_ids, video_ids, avg_rating, num_rating, {})
  transport.close()

def read_movie_info():
  socket = TSocket.TSocket("movie-info-service", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = MovieInfoService.Client(protocol)

  transport.open()
  for i in range(10):
    req_id = random.getrandbits(63)
    movie_id = "movie_id_" + str(random.randint(100000, 100004))
    client.ReadMovieInfo(req_id, movie_id, {})
  transport.close()

if __name__ == '__main__':
  try:
    wrtie_movie_info()
    read_movie_info()
  except ServiceException as se:
    print('%s' % se.message)
  except Thrift.TException as tx:
    print('ts %s' % tx.message)