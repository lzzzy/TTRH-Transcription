import ijson
import time

if __name__ == '__main__':
    start_time = None
    with open('./episodes/Episode 034 - Christmas New Year’s.json', encoding='utf-8', mode='r') as f:
        parser = ijson.parse(f)
        print('{"text":"', end='')
        for prefix, event, value in parser:
            if prefix.endswith('.confidence'):
                confidence = value
            elif prefix.endswith('.word_alternatives.item.start_time'):
                s_t = int(value)
                if not start_time:
                    start_time = s_t
            elif prefix.endswith('.word_alternatives.item.end_time'):
                #print('<br />', end='')
                end_time = int(value)
            #elif prefix.endswith('.word_alternatives.item.alternatives.item.word'):
            #    print('{}({}),'.format(value, confidence), end='')
            elif prefix.endswith('.alternatives.item.transcript'):
                print('<span class=\\\"timestamp\\\" data-timestamp=\\\"{}\\\">{}</span><br />'
                      .format(start_time,time.strftime('%H:%M:%S',time.gmtime(start_time))), end='')
                print('{}<br />'.format(value), end='')
                #print('<span class=\\\"timestamp\\\" data-timestamp=\\\"{}\\\">{}</span><br />'
                #      .format(end_time, time.strftime('%H:%M:%S', time.gmtime(end_time))), end='')
                start_time = None
        print('"}', end='')

