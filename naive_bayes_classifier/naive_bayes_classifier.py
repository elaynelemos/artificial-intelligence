import pandas as pd


class NaiveBayesClassifier:
    def __init__(self, training_data):
        self.classified_data = self.train_classifier(training_data)

    def train_classifier(self, training_data):
        structured_data = {
            'outlook': {},
            'temperature': {},
            'humidity': {},
            'wind': {}
        }
        df = pd.DataFrame(
            training_data,
            columns=['outlook', 'temperature', 'humidity', 'wind', 'play']
        )

        for key in structured_data.keys():
            grouped = df.groupby([key, 'play']).size().unstack().fillna(0)
            to_play = ['yes', 'no']

            structured_data[key] = {
                (feature, played): grouped[played][feature] for feature in grouped.index for played in to_play
            }

        structured_data['meta_data'] = {
            'data_length': df.shape[0],
            'yes': df['play'].value_counts()['yes'],
            'no': df['play'].value_counts()['no'],
        }

        return structured_data

    def prior_probability(self, to_play):
        ocurrences = self.classified_data['meta_data'][to_play]

        return ocurrences / self.classified_data['meta_data']['data_length']

    def dependent_probability(self, feature, state, play):
        condition_count = self.classified_data[feature][(state, play)]

        return condition_count / self.classified_data['meta_data'][play]

    def will_play(self, outlook, temperature, humidity, wind):
        features = ['outlook', 'temperature', 'humidity', 'wind']
        test_data_yes = 1
        test_data_no = 1

        for feature in features:
            test_data_yes *= self.dependent_probability(feature, eval(feature), 'yes')
            test_data_no *= self.dependent_probability(feature, eval(feature), 'no')

        yes_probability = test_data_yes*self.prior_probability('yes')
        no_probability = test_data_no*self.prior_probability('no')

        print(f'Play: {yes_probability}\n'
              f'Don\'t play: {no_probability}')

        return True if (yes_probability > no_probability) else False
