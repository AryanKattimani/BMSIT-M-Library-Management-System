import argparse, os, socket, sys, threading, time, webbrowser

def find_port(host, start=5000):
    for p in range(start,start+100):
        s=socket.socket(); s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:s.bind((host,p)); s.close(); return p
        except OSError:s.close()
    raise RuntimeError('No available local port found')

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--server',action='store_true'); parser.add_argument('--port',type=int,default=5000); args=parser.parse_args()
    if getattr(sys,'frozen',False) and 'server' in os.path.basename(sys.executable).lower(): args.server=True
    if getattr(sys,'frozen',False):
        root=os.path.dirname(sys.executable); os.environ.setdefault('BMSIT_LIBRARY_DATA',os.path.join(os.environ.get('APPDATA',os.path.expanduser('~')),'BMSIT-Library'))
    else: root=os.path.dirname(os.path.abspath(__file__))
    host='0.0.0.0' if args.server else '127.0.0.1'; port=find_port(host,args.port)
    from app import create_app
    app=create_app()
    url=('http://127.0.0.1:%d/'%port) if not args.server else ('http://127.0.0.1:%d/'%port)
    def open_browser(): time.sleep(1.0); webbrowser.open(url)
    if not args.server: threading.Thread(target=open_browser,daemon=True).start()
    print(f'BMSIT Library running at {url} (server mode={args.server})')
    app.run(host=host,port=port,debug=False,use_reloader=False,threaded=True)
if __name__=='__main__':main()
