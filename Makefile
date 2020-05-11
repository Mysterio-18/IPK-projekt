run:
	@python3.6	./weather.py	"$(api_key)"	"$(city)"
.DEFAULT:
	@2>/dev/null