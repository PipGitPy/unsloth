# Copyright 2023-present Daniel Han-Chen & the Unsloth team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    "INT_TO_FLOAT_MAPPER",
    "FLOAT_TO_INT_MAPPER",
]

__INT_TO_FLOAT_MAPPER = \
{
    "unsloth/mistral-7b-bnb-4bit" : (
        "unsloth/mistral-7b",
        "mistralai/Mistral-7B-v0.1",
    ),
    "unsloth/llama-2-7b-bnb-4bit" : (
        "unsloth/llama-2-7b",
        "meta-llama/Llama-2-7b-hf",
    ),
    "unsloth/llama-2-13b-bnb-4bit" : (
        "unsloth/llama-2-13b",
        "meta-llama/Llama-2-13b-hf",
    ),
    "unsloth/codellama-34b-bnb-4bit" : (
        "codellama/CodeLlama-34b-hf",
    ),
    "unsloth/zephyr-sft-bnb-4bit" : (
        "unsloth/zephyr-sft",
        "HuggingFaceH4/mistral-7b-sft-beta",
    ),
    "unsloth/tinyllama-bnb-4bit" : (
        "unsloth/tinyllama",
        "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    ),
    "unsloth/tinyllama-chat-bnb-4bit" : (
        "unsloth/tinyllama-chat",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    ),
    "unsloth/mistral-7b-instruct-v0.1-bnb-4bit" : (
        "unsloth/mistral-7b-instruct-v0.1",
        "mistralai/Mistral-7B-Instruct-v0.1",
    ),
    "unsloth/mistral-7b-instruct-v0.2-bnb-4bit" : (
        "unsloth/mistral-7b-instruct-v0.2",
        "mistralai/Mistral-7B-Instruct-v0.2",
    ),
    "unsloth/llama-2-7b-chat-bnb-4bit" : (
        "unsloth/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "unsloth/llama-2-7b-chat-bnb-4bit" : (
        "unsloth/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "unsloth/codellama-7b-bnb-4bit" : (
        "unsloth/codellama-7b",
        "codellama/CodeLlama-7b-hf",
    ),
    "unsloth/codellama-13b-bnb-4bit" : (
        "codellama/CodeLlama-13b-hf",
    ),
    "unsloth/yi-6b-bnb-4bit" : (
        "unsloth/yi-6b",
        "01-ai/Yi-6B",
    ),
    "unsloth/solar-10.7b-bnb-4bit" : (
        "upstage/SOLAR-10.7B-v1.0",
    ),
    "unsloth/gemma-7b-bnb-4bit" : (
        "unsloth/gemma-7b",
        "google/gemma-7b",
    ),
    "unsloth/gemma-2b-bnb-4bit" : (
        "unsloth/gemma-2b",
        "google/gemma-2b",
    ),
    "unsloth/gemma-7b-it-bnb-4bit" : (
        "unsloth/gemma-7b-it",
        "google/gemma-7b-it",
    ),
    "unsloth/gemma-2b-bnb-4bit" : (
        "unsloth/gemma-2b-it",
        "google/gemma-2b-it",
    ),
    "unsloth/mistral-7b-v0.2-bnb-4bit" : (
        "unsloth/mistral-7b-v0.2",
        "alpindale/Mistral-7B-v0.2-hf",
    ),
    "unsloth/gemma-1.1-2b-it-bnb-4bit" : (
        "unsloth/gemma-1.1-2b-it",
        "google/gemma-1.1-2b-it",
    ),
    "unsloth/gemma-1.1-7b-it-bnb-4bit" : (
        "unsloth/gemma-1.1-7b-it",
        "google/gemma-1.1-7b-it",
    ),
    "unsloth/Starling-LM-7B-beta-bnb-4bit" : (
        "unsloth/Starling-LM-7B-beta",
        "Nexusflow/Starling-LM-7B-beta",
    ),
    "unsloth/Hermes-2-Pro-Mistral-7B-bnb-4bit" : (
        "unsloth/Hermes-2-Pro-Mistral-7B",
        "NousResearch/Hermes-2-Pro-Mistral-7B",
    ),
    "unsloth/OpenHermes-2.5-Mistral-7B-bnb-4bit" : (
        "unsloth/OpenHermes-2.5-Mistral-7B",
        "teknium/OpenHermes-2.5-Mistral-7B",
    ),
    "unsloth/codegemma-2b-bnb-4bit" : (
        "unsloth/codegemma-2b",
        "google/codegemma-2b",
    ),
    "unsloth/codegemma-7b-bnb-4bit" : (
        "unsloth/codegemma-7b",
        "google/codegemma-7b",
    ),
    "unsloth/codegemma-7b-it-bnb-4bit" : (
        "unsloth/codegemma-7b-it",
        "google/codegemma-7b-it",
    ),
    "unsloth/llama-3-8b-bnb-4bit" : (
        "unsloth/llama-3-8b",
        "meta-llama/Meta-Llama-3-8B",
    ),
    "unsloth/llama-3-8b-Instruct-bnb-4bit" : (
        "unsloth/llama-3-8b-Instruct",
        "meta-llama/Meta-Llama-3-8B-Instruct",
    ),
    "unsloth/llama-3-70b-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B",
    ),
    "unsloth/llama-3-70b-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B-Instruct",
    ),
    "unsloth/Phi-3-mini-4k-instruct-bnb-4bit" : (
        "unsloth/Phi-3-mini-4k-instruct",
        "microsoft/Phi-3-mini-4k-instruct",
    ),
    "unsloth/mistral-7b-v0.3-bnb-4bit" : (
        "unsloth/mistral-7b-v0.3",
        "mistralai/Mistral-7B-v0.3",
    ),
    "unsloth/mistral-7b-instruct-v0.3-bnb-4bit" : (
        "unsloth/mistral-7b-instruct-v0.3",
        "mistralai/Mistral-7B-Instruct-v0.3",
    ),
    "unsloth/Phi-3-medium-4k-instruct-bnb-4bit" : (
        "unsloth/Phi-3-medium-4k-instruct",
        "microsoft/Phi-3-medium-4k-instruct",
    ),
    "unsloth/Qwen2-0.5B-bnb-4bit" : (
        "unsloth/Qwen2-0.5B",
        "Qwen/Qwen2-0.5B",
    ),
    "unsloth/Qwen2-0.5B-Instruct-bnb-4bit" : (
        "unsloth/Qwen2-0.5B-Instruct",
        "Qwen/Qwen2-0.5B-Instruct",
    ),
    "unsloth/Qwen2-1.5B-bnb-4bit" : (
        "unsloth/Qwen2-1.5B",
        "Qwen/Qwen2-1.5B",
    ),
    "unsloth/Qwen2-1.5B-Instruct-bnb-4bit" : (
        "unsloth/Qwen2-1.5B-Instruct",
        "Qwen/Qwen2-1.5B-Instruct",
    ),
    "unsloth/Qwen2-7B-bnb-4bit" : (
        "unsloth/Qwen2-7B",
        "Qwen/Qwen2-7B",
    ),
    "unsloth/Qwen2-7B-Instruct-bnb-4bit" : (
        "unsloth/Qwen2-7B-Instruct",
        "Qwen/Qwen2-7B-Instruct",
    ),
    "unsloth/Qwen2-70B-bnb-4bit" : (
        "Qwen/Qwen2-70B",
    ),
    "unsloth/Qwen2-70B-Instruct-bnb-4bit" : (
        "Qwen/Qwen2-70B-Instruct",
    ),
    "mistralai/Codestral-22B-v0.1" : (
        "mistral-community/Codestral-22B-v0.1",
    ),
    "unsloth/gemma-2-9b-bnb-4bit" : (
        "unsloth/gemma-2-9b",
        "google/gemma-2-9b",
    ),
    "unsloth/gemma-2-27b-bnb-4bit" : (
        "unsloth/gemma-2-27b",
        "google/gemma-2-27b",
    ),
    "unsloth/gemma-2-9b-it-bnb-4bit" : (
        "unsloth/gemma-2-9b-it",
        "google/gemma-2-9b-it",
    ),
    "unsloth/gemma-2-27b-it-bnb-4bit" : (
        "unsloth/gemma-2-27b-it",
        "google/gemma-2-27b-it",
    ),
    "unsloth/Phi-3-mini-4k-instruct-v0-bnb-4bit" : ( # Old Phi pre July
        "unsloth/Phi-3-mini-4k-instruct-v0",
    ),
    "unsloth/Mistral-Nemo-Instruct-2407-bnb-4bit" : ( # New 12b Mistral models
        "unsloth/Mistral-Nemo-Instruct-2407",
        "mistralai/Mistral-Nemo-Instruct-2407",
    ),
    "unsloth/Mistral-Nemo-Base-2407-bnb-4bit" : ( # New 12b Mistral models
        "unsloth/Mistral-Nemo-Base-2407",
        "mistralai/Mistral-Nemo-Base-2407",
    ),
    "unsloth/llama-3.1-8b-bnb-4bit" : (
        "unsloth/llama-3.1-8b",
        "meta-llama/Meta-Llama-3.1-8B",
    ),
    "unsloth/llama-3.1-8b-Instruct-bnb-4bit" : (
        "unsloth/llama-3.1-8b-Instruct",
        "meta-llama/Meta-Llama-3.1-8B-Instruct",
    ),
    "unsloth/llama-3.1-70b-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-70B",
    ),
    "unsloth/llama-3.1-70b-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-70B-Instruct",
    ),
}

INT_TO_FLOAT_MAPPER = {}
FLOAT_TO_INT_MAPPER = {}

for key, values in __INT_TO_FLOAT_MAPPER.items():
    INT_TO_FLOAT_MAPPER[key] = values[0]

    for value in values:
        FLOAT_TO_INT_MAPPER[value] = key
    pass

    # Get lowercased
    lowered_key = key.lower()
    INT_TO_FLOAT_MAPPER[lowered_key] = values[0].lower()

    for value in values:
        FLOAT_TO_INT_MAPPER[value.lower()] = lowered_key
    pass
pass
