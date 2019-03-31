import tags_pool
import time
print(int(time.time()))
test_pool = tags_pool.Database("./test_pool.ini")
a = test_pool.create_tags(3)

for x in a:
    print(x)
    test_pool.tags[x].gen_qrcode()

test_pool.save_tags()
