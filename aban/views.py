#!/usr/bin/env python
# encoding: utf8
#
# Copyright © BJ Cardon <bj dot car dot don at gmail dot com>,
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. Neither the name of the owner nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Integer
from spyne.model.complex import Iterable
from spyne.service import Service
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoComplexModel
from aban.models import Note


class ComplexNote(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = Note


class NoteService(Service):
    @rpc(Integer, _returns=ComplexNote)
    def get_note(ctx, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise ResourceNotFoundError('ComplexNote')

    @rpc(Integer, _returns=Iterable(ComplexNote))
    def get_notes(ctx, pk):
        try:
            return Note.objects.all()
        except Note.DoesNotExist:
            raise ResourceNotFoundError('ComplexNote')

    @rpc(ComplexNote, _returns=ComplexNote)
    def create_note(ctx, note):
        try:
            return Note.objects.create(**note.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError('ComplexNote')


app = Application([NoteService],
                  'epg.aban',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11(),
                  )

note_soap_service = csrf_exempt(DjangoApplication(app))
