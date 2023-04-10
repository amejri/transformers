# Copyright 2020 The HuggingFace Team. All rights reserved.
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

from typing import TYPE_CHECKING

from ...utils import (
    OptionalDependencyNotAvailable,
    _LazyModule,
    is_sentencepiece_available,
    is_tokenizers_available,
    is_torch_available,
)


_import_structure = {
    "configuration_hypermixer": ["HYPER_MIXER_PRETRAINED_CONFIG_ARCHIVE_MAP", "HyperMixerConfig"],
    "tokenization_hypermixer": ["HyperMixerTokenizer"],
}

try:
    if not is_sentencepiece_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_hypermixer"] = ["HyperMixerTokenizer"]


try:
    if not is_tokenizers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_hypermixer_fast"] = ["HyperMixerTokenizerFast"]

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_hypermixer"] = [
        "HYPER_MIXER_PRETRAINED_MODEL_ARCHIVE_LIST",
        "HyperMixerForMaskedLM",
        "HyperMixerForMultipleChoice",
        "HyperMixerForNextSentencePrediction",
        "HyperMixerForPreTraining",
        "HyperMixerForQuestionAnswering",
        "HyperMixerForSequenceClassification",
        "HyperMixerForTokenClassification",
        "HyperMixerLayer",
        "HyperMixerLMHeadModel",
        "HyperMixerModel",
        "HyperMixerPreTrainedModel",
    ]

if TYPE_CHECKING:
    from .configuration_hypermixer import HYPER_MIXER_PRETRAINED_CONFIG_ARCHIVE_MAP, HyperMixerConfig
    from .tokenization_hypermixer import HyperMixerTokenizer


    try:
        if not is_sentencepiece_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_hypermixer import HyperMixerTokenizer

    try:
        if not is_tokenizers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_hypermixer_fast import HyperMixerTokenizerFast

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_hypermixer import (
            HYPER_MIXER_PRETRAINED_MODEL_ARCHIVE_LIST,
            HyperMixerForMaskedLM,
            HyperMixerForMultipleChoice,
            HyperMixerForNextSentencePrediction,
            HyperMixerForPreTraining,
            HyperMixerForQuestionAnswering,
            HyperMixerForSequenceClassification,
            HyperMixerForTokenClassification,
            HyperMixerLayer,
            HyperMixerModel,
            HyperMixerPreTrainedModel,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
