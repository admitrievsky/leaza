from datetime import datetime, timezone


def format_string_rus(n, measure, endings, endings10_20):
    n = int(n)
    if measure:
        return '%d %s%s' % (n, measure, endings[n % 10] if n < 10 or n > 20 else endings10_20)
    else:
        return '%d %s' % (n, endings[n % 10] if n < 10 or n > 20 else endings10_20)


def time_elapsed(from_when):
    delta = (datetime.now(timezone.utc) - from_when).total_seconds()

    if delta < 60*60:
        return format_string_rus(delta / 60, 'минут', ['', 'у', "ы", "ы", "ы", '', '', '', '', ''], '')
    elif delta < 24 * 60*60:
        return format_string_rus(delta / 3600, 'час', ['ов', '', "а", "а", "а", 'ов', 'ов', 'ов', 'ов', 'ов'], 'ов')
    elif delta < 32 * 24 * 3600:
        return format_string_rus(delta / (24 * 3600), None, ['дней', 'день', "дня", "дня", "дня", 'дней', 'дней', 'дней', 'дней', 'дней'], 'дней')
    else:
        return format_string_rus(delta / (24 * 3600 * 32), 'месяц', ['ев', '', "а", "а", "а", 'ев', 'ев', 'ев', 'ев', 'ев'], 'ев')


def get_comment_count(n):
    return format_string_rus(n, 'комментари', ['ев', "й", "я", "я", "я", "ев", "ев", "ев", "ев", "ев"], "ев")
