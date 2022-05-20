from knowledge_base.models import Strategy
from django import forms


INTERVALS = (
    ('CANDLE_INTERVAL_1_MIN', '1 минута'),
    ('CANDLE_INTERVAL_5_MIN', '5 минут'),
    ('CANDLE_INTERVAL_15_MIN', '15 минут'),
    ('CANDLE_INTERVAL_HOUR', '1 час'),
    ('CANDLE_INTERVAL_DAY', '1 день'),
)


class StrategyForm(forms.Form):
    """
    Form to choose what strategy to use
    """
    strategy = forms.ModelChoiceField(queryset=Strategy.objects.all())


class BacktestStockForm(forms.Form):
    """
    Form for configuring stock, timeframe and period
    """
    stock = forms.CharField(max_length=50, label='Инструмент')
    timeframe = forms.ChoiceField(choices=INTERVALS, label='Интервал')
    start_date = forms.DateTimeField(label='Начало периода')
    end_date = forms.DateTimeField(label='Конец периода')

