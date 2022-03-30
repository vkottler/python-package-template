###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: edit generate test test-cli test-interactive clean clean-output yaml

generate: | $(VENV_CONC)
	$(PYTHON_BIN)/cookiecutter \
		-o $($(PROJ)_DIR)/.. \
		$($(PROJ)_DIR)

OUTPUT := package-name

COMMON_ARGS := -o $($(PROJ)_DIR) $($(PROJ)_DIR)

test-cli: clean-output | $(VENV_CONC)
	$(PYTHON_BIN)/cookiecutter \
		--no-input \
		$(COMMON_ARGS)

test: test-cli

test-interactive: clean-output | $(VENV_CONC)
	$(PYTHON_BIN)/cookiecutter $(COMMON_ARGS)

clean-output:
	rm -rf $($(PROJ)_DIR)/$(OUTPUT)

clean: clean-output $(DZ_PREFIX)clean $(PY_PREFIX)clean

yaml: $(YAML_PREFIX)lint-local $(YAML_PREFIX)lint-manifest.yaml

edit: $(PY_PREFIX)edit
