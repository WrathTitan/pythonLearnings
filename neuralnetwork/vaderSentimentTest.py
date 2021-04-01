from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
def sentiment_scores(sentence): 

    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    print("Sentence Overall Rated As", end = " ") 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 

    
if __name__ == "__main__" : 
    
    sentence = "Geeks For Geeks is the best portal for computer science engineering students." 
    print("\n1st statement :" + sentence) 
    sentiment_scores(sentence) 
  
    sentence = "study is going on as usual"
    print("\n2nd Statement :"+sentence)
    sentiment_scores(sentence) 
  
    sentence = "I am vey sad today."
    print("\n3rd Statement :"+sentence)
    sentiment_scores(sentence) 