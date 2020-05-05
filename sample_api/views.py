from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Parent
from .serializer import ParentSerializer

class NestedListView(generics.ListAPIView):
    """
    ネストしたリソースのlistメソッド
    listだけ使いたいのでgenerics.ListAPIViewを使用
    """
    pagination_class = PageNumberPagination
    serializer_class = ParentSerializer
    # クエリ―パラメータをfilterの検索条件に変換するdict
    CONDITION_KEYS = {
        'parent_column': 'parent_column__contains',
        'child1_column': 'child1s__child1_column__contains',
        'child2_column': 'child2s__child2_column__contains',
        }

    def get_queryset(self):
        """
        テーブルとフロントの設計を自分が決められない場合
        後々、複雑なQuerySetを書くことになるかもしれないので、
        ゴニョゴニョできる場所で定義しておく。
        """
        # 検索条件のdict
        condition_dict = {}
        for key, val in self.request.query_params.items():
            # query_paramsのkeyに検索条件の項目があったらfilter用のkeyに変換する
            # ホントはlamdaとか使った方がカッコイイ
            if key in self.CONDITION_KEYS:
                condition_dict[self.CONDITION_KEYS[key]] = val

        queryset = Parent.objects.filter(**condition_dict).order_by('id').prefetch_related().distinct()

        return queryset

    def list(self, request, *args, **kwargs):
        """
        listメソッドをオーバライド
        """
        # querysetにpaginationを適用
        page_qs = self.paginate_queryset(self.get_queryset())
        # serializeを取得
        serializer = self.get_serializer(page_qs, many=True)
        # paginationつきで返却
        return self.get_paginated_response(serializer.data)


