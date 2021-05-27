import StockTools

StockTool = StockTools.StockData()
StockTool.requestJSON('AAPL')
print(StockTool.results)