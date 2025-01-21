#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Define the size to allocate: 1GB (1024 * 1024 * 1024 bytes)
    size_t size = 1024 * 1024 * 1024;

    // Allocate memory
    char *buffer = (char *)malloc(size);

    if (buffer == NULL) {
        printf("Failed to allocate 1GB of memory.\n");
        return 1;
    }

    printf("Successfully reserved 1GB of memory.\n");

    // Optionally, initialize the memory (e.g., to avoid lazy allocation by the OS)
    memset(buffer, 0, size);

    printf("Memory is now initialized.\n");

    // Simulate temporary usage
    printf("Press Enter to release the memory...");
    getchar();

    // Free the allocated memory
    free(buffer);
    printf("Memory released back to the system.\n");

    return 0;
}