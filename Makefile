###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: generate test clean yaml

generate: | $(VENV_CONC)
	$(PYTHON_BIN)/cookiecutter \
		-o $($(PROJ)_DIR)/.. \
		$($(PROJ)_DIR)

OUTPUT := package-name

test: | $(VENV_CONC)
	rm -rf $($(PROJ)_DIR)/$(OUTPUT)
	$(PYTHON_BIN)/cookiecutter \
		-o $($(PROJ)_DIR) \
		--no-input \
		$($(PROJ)_DIR)

clean: $(DZ_PREFIX)clean $(PY_PREFIX)clean
	rm -rf $($(PROJ)_DIR)/$(OUTPUT)

yaml: $(YAML_PREFIX)lint-local $(YAML_PREFIX)lint-manifest.yaml
