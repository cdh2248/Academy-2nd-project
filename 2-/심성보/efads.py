




if __name__ == '__main__':
    pass

print(__name__)

if __name__ == '__main__':
    # app.run(host='localhost')
    t = threading.Thread(target=app.run(host='192.168.30.240'), daemon=True)
    t.start()










