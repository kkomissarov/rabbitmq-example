1. Install requirements
```
pip install -r requirements.txt
```

2. Run docker-compose
```
docker-compose up -d
```

3. To send message to queue run sender.py
```
python sender.py
```

4. To receive messages from queue run receiver.py
```
python receiver.py
```