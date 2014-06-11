from __future__ import print_function, unicode_literals

import pickle
import luigi
from luigi import Task, Parameter, LocalTarget

from ops.transform import pdf_text, stop_words
from ops.extract import extract_path
from tasks.extract import ExtractMinutes

class TransformPDF(Task):
    date = Parameter(default=None)

    def requires(self):
        return ExtractMinutes(date=self.date)

    def output(self):
        return LocalTarget('{}/raw.text'.format(\
                                extract_path(self.date)))

    def run(self):
        with self.input().open('r') as I:
            text = pdf_text(I)
            with self.output().open('w') as O:
                O.write(text.encode('utf-8'))

class StopListText(luigi.Task):
    date = Parameter(default=None)

    def requires(self):
        return TransformPDF(self.date)

    def output(self):
        return LocalTarget('{}/cleaned.txt'.format(\
                                extract_path(self.date)))

    def run(self):
        with self.input().open('r') as I:
            text = stop_words(I.read())
            with self.output().open('w') as O:
                O.write(text.encode('utf-8'))


class CreateTokens(luigi.Task):
    date = luigi.Parameter()
    
    def requires(self):
        return StopListText(self.date)

    def output(self):
        return LocalTarget('{}/tokens.pkl'.format(\
                            extract_path(self.date)))

    def run(self):
        with self.input().open('r') as I:
            raw_text = I.read()

            tokens_counted = create_tokens(raw_text)
            with self.output().open('w') as O:
                pickle.dump(tokens_counted, O)
                

class CreateTokenLinks(luigi.Task):
    date = luigi.Parameter()

    def requires(self):
        return StopListText(self.date)

    def output(self):
        return LocalTarget('{}/token_links.pkl'.format(\
                        extract_path(self.date)))

    def run(self):
        with self.input().open('r') as I:
            raw_text = I.read()

            text = remove_punctuation(raw_text)
            text = stop_word_placeheld(text)

            links = link_op(text, distance=25)
            with self.output().open('w') as O:
                pickle.dump(links, O)


class YearList(luigi.Task):
    date = Parameter(default=None)
            
    def requires(self):
        pass

    def output(self):
        pass

    def run(self):
        pass 

if __name__ == '__main__':
    luigi.run()
