import pandas as pd
import numpy as np
from collections import Counter
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from wordcloud import WordCloud
from typing import Dict, List, Union

class TextEDA:
    def __init__(self, generated_texts: List[str]):
        """
        Initialize TextEDA with list of generated texts
        
        Args:
            generated_texts (List[str]): List of text descriptions generated from video frames
        """
        self.texts = generated_texts
        
        # Initialize NLP tools
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('averaged_perceptron_tagger')
        self.nlp = spacy.load('en_core_web_sm')
        self.stop_words = set(stopwords.words('english'))
        
    def basic_stats(self) -> Dict:
        """
        Calculate basic text statistics
        """
        word_counts = [len(str(text).split()) for text in self.texts]
        char_counts = [len(str(text)) for text in self.texts]
        sentence_counts = [len(sent_tokenize(str(text))) for text in self.texts]
        
        stats = {
            'total_descriptions': len(self.texts),
            'avg_word_count': np.mean(word_counts),
            'std_word_count': np.std(word_counts),
            'avg_char_length': np.mean(char_counts),
            'avg_sentence_count': np.mean(sentence_counts),
            'unique_words': len(set(' '.join(self.texts).split())),
            'word_count_percentiles': {
                '25th': np.percentile(word_counts, 25),
                '50th': np.percentile(word_counts, 50),
                '75th': np.percentile(word_counts, 75)
            }
        }
        return stats
    
    def content_analysis(self) -> Dict:
        """
        Analyze text content patterns
        """
        # Combine all texts
        all_text = ' '.join(self.texts)
        words = word_tokenize(all_text.lower())
        
        # Remove stopwords and punctuation
        clean_words = [word for word in words if word.isalnum() and word not in self.stop_words]
        
        # Get POS tags
        pos_tags = nltk.pos_tag(clean_words)
        
        analysis = {
            'most_common_words': Counter(clean_words).most_common(20),
            'most_common_bigrams': Counter(ngrams(clean_words, 2)).most_common(10),
            'pos_distribution': Counter(tag for word, tag in pos_tags),
            'vocabulary_richness': len(set(clean_words)) / len(clean_words)
        }
        return analysis
    
    def sentiment_analysis(self) -> Dict:
        """
        Analyze sentiment patterns in texts
        """
        sentiments = [TextBlob(str(text)).sentiment for text in self.texts]
        
        analysis = {
            'avg_polarity': np.mean([s.polarity for s in sentiments]),
            'avg_subjectivity': np.mean([s.subjectivity for s in sentiments]),
            'sentiment_distribution': {
                'positive': len([s for s in sentiments if s.polarity > 0]),
                'neutral': len([s for s in sentiments if s.polarity == 0]),
                'negative': len([s for s in sentiments if s.polarity < 0])
            }
        }
        return analysis
    
    def topic_analysis(self) -> Dict:
        """
        Extract main topics and entities
        """
        docs = list(self.nlp.pipe(self.texts))
        
        # Extract named entities
        all_entities = []
        for doc in docs:
            all_entities.extend([(ent.text, ent.label_) for ent in doc.ents])
        
        # Extract noun phrases
        noun_phrases = []
        for doc in docs:
            noun_phrases.extend([chunk.text for chunk in doc.noun_chunks])
        
        analysis = {
            'named_entities': Counter(all_entities).most_common(15),
            'common_noun_phrases': Counter(noun_phrases).most_common(15)
        }
        return analysis
    
    def plot_word_distribution(self) -> None:
        """
        Plot word count distribution
        """
        word_counts = [len(str(text).split()) for text in self.texts]
        
        plt.figure(figsize=(10, 6))
        sns.histplot(word_counts, bins=30)
        plt.title('Distribution of Word Counts')
        plt.xlabel('Number of Words')
        plt.ylabel('Frequency')
        plt.show()
    
    def plot_wordcloud(self) -> None:
        """
        Generate and plot wordcloud
        """
        all_text = ' '.join(self.texts)
        wordcloud = WordCloud(
            width=800, height=400,
            background_color='white',
            stopwords=self.stop_words
        ).generate(all_text)
        
        plt.figure(figsize=(15, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Generated Descriptions')
        plt.show()
    
    def plot_sentiment_distribution(self) -> None:
        """
        Plot sentiment distribution
        """
        sentiments = [TextBlob(str(text)).sentiment.polarity for text in self.texts]
        
        plt.figure(figsize=(10, 6))
        sns.histplot(sentiments, bins=30)
        plt.title('Distribution of Sentiment Polarity')
        plt.xlabel('Polarity')
        plt.ylabel('Frequency')
        plt.show()
    
    def plot_pos_distribution(self) -> None:
        """
        Plot distribution of Parts of Speech
        """
        all_text = ' '.join(self.texts)
        pos_tags = nltk.pos_tag(word_tokenize(all_text))
        pos_counts = Counter(tag for word, tag in pos_tags)
        
        plt.figure(figsize=(12, 6))
        plt.bar(pos_counts.keys(), pos_counts.values())
        plt.title('Distribution of Parts of Speech')
        plt.xticks(rotation=45)
        plt.xlabel('POS Tag')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

def run_eda(texts: List[str]) -> Dict:
    """
    Run complete EDA and return all results
    
    Args:
        texts (List[str]): List of generated text descriptions
    
    Returns:
        Dict: Complete EDA results
    """
    analyzer = TextEDA(texts)
    
    # Collect all analyses
    results = {
        'basic_statistics': analyzer.basic_stats(),
        'content_analysis': analyzer.content_analysis(),
        'sentiment_analysis': analyzer.sentiment_analysis(),
        'topic_analysis': analyzer.topic_analysis()
    }
    
    # Generate plots
    print("\nGenerating visualizations...")
    analyzer.plot_word_distribution()
    analyzer.plot_wordcloud()
    analyzer.plot_sentiment_distribution()
    analyzer.plot_pos_distribution()
    
    return results

# Example usage
if __name__ == "__main__":
    # Example texts (replace with your actual generated texts)
    example_texts = [
        "A person is walking through a park on a sunny day.",
        "The video shows a busy street with cars and pedestrians.",
        "A group of friends are enjoying dinner at a restaurant."
    ]
    
    # Run EDA
    eda_results = run_eda(example_texts)
    
    # Print summary of results
    print("\nEDA Results Summary:")
    print(f"\nTotal Descriptions: {eda_results['basic_statistics']['total_descriptions']}")
    print(f"Average Word Count: {eda_results['basic_statistics']['avg_word_count']:.2f}")
    print(f"Vocabulary Richness: {eda_results['content_analysis']['vocabulary_richness']:.2f}")
    print(f"Average Sentiment Polarity: {eda_results['sentiment_analysis']['avg_polarity']:.2f}")
    
    print("\nTop 5 Most Common Words:")
    for word, count in eda_results['content_analysis']['most_common_words'][:5]:
        print(f"- {word}: {count}")
