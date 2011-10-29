from songs import app, connection, render_template
import datetime
import json



@app.route('/')
def index():
    
    db = connection.song_test
    
    songs = db.songs
    
    song = {
    	"name": "Tuesday",
    	"album": "A Comfortable Sleep",
    	"artist": "Paper Aeroplanes",
    	"occasions": [
    		{
    			"type":"day", 
    			"value":"tuesday",
    			"excerpt":"On a Tuesday morning in July<br />"
    					+ "I was bright and breathing, unwilling to die."
    		},
    		{
    			"type":"day",
    			"value":"tuesday",
    			"excerpt":"By a Tuesday evening, you replied<br />"
    					+ "Every word, every color analyzed."
    		},
    		{
    			"type":"day",
    			"value":"wednesday",
    			"excerpt":"Maybe then I can just move on,<br />"
    					+ "On a Wednesday morning in July."
    		},
    		{
    			"type":"month",
    			"value":"july",
    			"excerpt":"On a Tuesday morning in July<br />"
    					+ "I was bright and breathing, unwilling to die."
    		},
    		{
    			"type":"month",
    			"value":"july",
    			"excerpt":"Maybe then I can just move on,<br />"
    					+ "On a Wednesday morning in July."
    		}
    	]
    }
    
#    songs.insert(song)
    
    result = songs.find({"name":"Tuesday"})[0]
    return render_template('test.html', result=result)
    
    
    
    