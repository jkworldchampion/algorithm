#include <stdio.h>
#include <stdlib.h>

int main() {
    // 1. 2차원 배열의 크기를 5 x 3으로 미리 알고 있을 경우
    int array1[5][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {10, 11, 12},
        {13, 14, 15}
    };

    // 2. 2차원 배열의 크기를 사용자로부터 입력받아 동적으로 할당할 경우
    int rows, cols;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &cols);
    int **array2 = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        array2[i] = (int *)malloc(cols * sizeof(int));
    }
    int count = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            array2[i][j] = count++;
        }
    }

    // 3. 두 배열의 원소의 주소 값과 저장된 데이터를 출력하기
    // 각각의 배열에 대해 출력된 주소 공간이 항상 연속적인지를 확인하라.
    printf("array1\n");
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%p: %d  ", &array1[i][j], array1[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    printf("array2\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%p: %d  ", &array2[i][j], array2[i][j]);
        }
        printf("\n");
    }

    // 4. 동적으로 할당한 메모리를 해제하기
    for (int i = 0; i < rows; i++) {
        free(array2[i]);
    }
    free(array2);


    // 5. 불연속의 상황에 따른 연속적인 메모리 공간 할당
    // 간단한 방법
    int *fullish_array = (int *)malloc(rows * cols * sizeof(int)); 

    int **array3 = (int **)malloc(rows * sizeof(int *));
    array3[0] = (int *)malloc(rows * cols * sizeof(int));

    for (int i = 1; i < rows; i++) {
        array3[i] = array3[i - 1] + cols;
    }
    count = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            array3[i][j] = count++;
        }
    }

    // 6. 세 번째 배열의 원소의 주소 값과 저장된 데이터를 출력하기
    printf("array3\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%p: %d  ", &array3[i][j], array3[i][j]);
        }
        printf("\n");
    }

    // 7. 동적으로 할당한 메모리를 해제하기
    free(array3[0]);
    free(array3);


    

    return 0;
    
}
