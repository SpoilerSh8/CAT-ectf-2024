
# function to check required arguments
check_defined = \
	$(strip $(foreach 1,$1, \
		$(call __check_defined,$1)))
__check_defined = \
	$(if $(value $1),, \
		$(error Undefined $1))	
		
all:
	poetry run python3 param.py
clean:
	rm -f ../global_secrets.h
	rm -f cat.h
	rm -rf ../build
	rm -f ../application_processor/inc/ectf_params.h
	rm -f ../component/inc/ectf_params.h
	
	