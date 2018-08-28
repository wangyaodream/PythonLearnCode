def fetcher(obj,index):
    return obj[index]

x = 'loveisgod'

def after():
    try:
        fetcher(x,10)
    except:
        print('Something wrong')
    finally:
        print('This is finally block')

if __name__=="__main__":
    after()